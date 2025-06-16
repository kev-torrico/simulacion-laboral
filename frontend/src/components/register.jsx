import React, { useState } from "react";
import { Button, Card, Field, Input, Stack, Center } from "@chakra-ui/react";
import { Toaster, toaster } from "./ui/toaster";
import { BASE_URL } from "../App";

function Register() {
  const [inputs, setInputs] = useState({
    name: "",
    email: "",
    password: "",
  });

  const handleCreateUser = async (e) => {
    e.preventDefault();
    if (!inputs.email.includes("@")) {
      return toaster.create({
        title: "Invalid email",
        type: "error",
        duration: 3000,
      });
    }
    if (inputs.password.length < 6) {
      return toaster.create({
        title: "Short password",
        type: "error",
        duration: 3000,
      });
    }

    try {
      const response = await fetch(BASE_URL + "/api/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(inputs),
      });
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error);
      }
      toaster.create({
        title: "User created succesfully",
        type: "success",
        duration: 3000,
      });
      setInputs({ name: "", email: "", password: "" });
    } catch (error) {
      toaster.create({
        title: "An error has occurred",
        type: "error",
        description: error.message,
        duration: 4000,
      });
    }
  };

  return (
    <>
      <Center mt={100}>
        <Card.Root maxW="sm">
          <Card.Header>
            <Card.Title>Sign up</Card.Title>
            <Card.Description>
              Fill in the form below to create an account
            </Card.Description>
          </Card.Header>
          <Card.Body>
            <Stack gap="4" w="full">
              <Field.Root>
                <Field.Label>First Name</Field.Label>
                <Input
                  value={inputs.name}
                  onChange={(e) =>
                    setInputs({ ...inputs, name: e.target.value })
                  }
                />
              </Field.Root>
              <Field.Root>
                <Field.Label>Email</Field.Label>
                <Input
                  value={inputs.email}
                  onChange={(e) =>
                    setInputs({ ...inputs, email: e.target.value })
                  }
                />
              </Field.Root>
              <Field.Root>
                <Field.Label>Password</Field.Label>
                <Input
                  value={inputs.password}
                  onChange={(e) =>
                    setInputs({ ...inputs, password: e.target.value })
                  }
                />
              </Field.Root>
            </Stack>
          </Card.Body>
          <Card.Footer justifyContent="flex-end">
            <Button variant="outline">Cancel</Button>
            <Button
              variant="solid"
              onClick={(e) => {
                handleCreateUser(e);
              }}
            >
              Sign in
            </Button>
          </Card.Footer>
        </Card.Root>
        <Toaster />
      </Center>
    </>
  );
}

export default Register;
